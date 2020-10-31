var embed_county = document.getElementById("embed_inner");
var embed_outer = document.getElementById("embed_outer");
var main_break = false;
var box_super = false;

// getting long and lat
window.onload = function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	} else {
		console.log("null");
	}
	navigator.geolocation.watchPosition(
		function (position) {
      // location access accepted => loads lat, long into fips_lookup
      // $.post( "/", { county_name: lat, state_code: long });
      // console.log("LOCATION ACCESS GRANTED \nLatitude: " + lat + "\nLongitude: " + long);
      fips_lookup(lat, long);
    },
    function (box_super){
      if(box_super==true){
        console.log('ssss')
        fips_lookup(box_data.x, box_data.y)
      }else{
        $.post( "/", { county_name: "world", state_code: "global" })

      // var lat = 55.7558; // uncomment to test international locations
      // var long = 37.6173; //! default testing for international ==> Москва (Moscow) 
      // fips_lookup(lat, long)

      covid_nametag.innerHTML = "World COVID-19 News"
      location_err.innerHTML ="Location access was denied. Showing global news";
      embed_county.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/world-map/?embed=world#/" frameborder="0" scrolling="no" ></iframe>'
      }
    },
		function (error) {
      // handles location access denied => defaults location to stanford
      $.post( "/", { county_name: "world", state_code: "global" })

      // var lat = 55.7558; // uncomment to test international locations
      // var long = 37.6173; //! default testing for international ==> Москва (Moscow) 
      // fips_lookup(lat, long)

      covid_nametag.innerHTML = "World COVID-19 News"
      location_err.innerHTML ="Location access was denied. Showing global news";
      embed_county.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/world-map/?embed=world#/" frameborder="0" scrolling="no" ></iframe>'
    }
  );
};


function showPosition(position) {
    lat = position.coords.latitude;
    long = position.coords.longitude;
    if (typeof box_data !== 'undefined') {
      lat = box_data.x
      long = box_data.y
    }  
    
    fips_lookup();
}

function cc_int(country_code) {
	// feeding in long and lat to convert into FIPS and county

	var cc_rest =
		"https://restcountries.eu/rest/v2/alpha/" + country_code + "#";
	var settings = {
		async: true,
		crossDomain: true,
		url: cc_rest,
		method: "GET",
  };

	// reading in json object and extracting fips, county and state
	$.ajax(settings).done(function (response) {
    embed_county.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/world-map/?embed=country#/country/' + (response['numericCode']) + '" frameborder="0" scrolling="no" ></iframe>'
    embed_outer.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/world-map/?embed=world#/" frameborder="0" scrolling="no" ></iframe>'
    // embed_county.innerHTML = '<iframe style="width: 600px; height: 815px" src="https://covid19.biglocalnews.org/world-map/?embed=world#/" frameborder="0" scrolling="no" ></iframe>'
  });
}


function international(geolat, geolong){
  var reverseGeocoder=new BDCReverseGeocode();
      
  reverseGeocoder.getClientLocation(function(result) {
      console.log(result);
  });

  reverseGeocoder.getClientLocation({
      latitude: geolat,
      longitude: geolong,
  },function(result) {
      $.post( "/", { county_name: result['city'], state_code: result['countryName'] });
      console.log(result['city'] + ", " + result['countryName'])

      // increase index to see more in depth data (if bln gets a more low level view for cases)
      // console.log(result['localityInfo']['administrative'][index]['isoCode']) //! test data here 
      
      cc_int(result['localityInfo']['administrative'][0]['isoCode'])
      document.getElementById("location").value = result['city'] + ", " + result['countryName'];
      covid_nametag.innerHTML = "COVID-19 News In " + result['city'] + ", " + result['countryName'];
  });

  reverseGeocoder.localityLanguage='es';

  reverseGeocoder.getClientCoordinates(function(result) {
      console.log(result);
  });
}


function fips_lookup(geolat, geolong) {
  console.log('starting fips lookup...');
	// feeding in long and lat to convert into FIPS and county

	var fips_url =
		"https://geo.fcc.gov/api/census/area?lat=" +
		geolat +
		"&lon=" +
		geolong +
    "&format=json";
    console.log(fips_url)
	var settings = {
		async: true,
		crossDomain: true,
		url: fips_url,
		method: "GET",
  };

	// reading in json object and extracting fips, county and state
	$.ajax(settings).done(function (response) {
    console.log(response);

    if(response.results.length == 0){
      international(geolat, geolong)
    }
    else{
      // document.getElementById("location").value = response.results[0].county_name + " County, " + response.results[0].state_code;
      covid_nametag.innerHTML = "COVID-19 News In " + response.results[0].county_name + " County, " + response.results[0].state_code;
      
      embed_county.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/county-maps/index.html?embed=stateCounty#/county/' + response.results[0].county_fips + '"frameborder="0" scrolling="yes"></iframe>';
      embed_outer.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/county-maps/index.html?embed=usa#/" frameborder="0" scrolling="yes"></iframe></iframe>'    
      // document.getElementById("main_post").submit()
      
      document.getElementById("location").value = response.results[0].county_name + " County, " + response.results[0].state_code;
      console.log(document.getElementById("location").value)
      // document.getElementById("main_post").submit()

      $.post( "/", { county_name: response.results[0].county_name, state_code: response.results[0].state_code });
    }
  });
}

