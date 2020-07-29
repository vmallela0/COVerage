var embed_county = document.getElementById("embed");
var main_break = false;

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
      
			// console.log("LOCATION ACCESS GRANTED \nLatitude: " + lat + "\nLongitude: " + long);
      fips_lookup(lat, long);
		},
		function (error) {
			// handles location access denied => defaults location to stanford
			if (error.code == error.PERMISSION_DENIED) {
				// alert("Location access was denied. Deafulting location to Stanford, CA...")
				// var lat = 37.431313849999995;
        // var long = -122.16936535498309; // stanford default
        
        var lat = 32.7157;
        var long = -117.1611; //! default for ppl testing @ stanford (San Diego)

        // var lat = 51.5074;
        // var long = -0.1278; //! default testing for international ==> London

				console.log("LOCATION ACCESS DENIED");
				console.log(
					"default latitude: " + lat + "\ndefault longitude: " + long
				);
				fips_lookup(lat, long);
        location_err.innerHTML =
          "Location access was denied. Defaulted location to London, England";
					// "Location access was denied. Defaulted location to Stanford, CA";
				userlocation.innerHTML = "COVID-19 News in ";
			}
    }
  );
};

("use strict");

// const fs = require('fs');

function showPosition(position) {
	lat = position.coords.latitude;
	long = position.coords.longitude;
  fips_lookup();
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
      console.log(result['city'] + ", " + result['countryName'])
      document.getElementById("location").value = result['city'] + ", " + result['countryName'];
      covid_nametag.innerHTML = "COVID-19 News In " + result['city'] + ", " + result['countryName'];
      $.post( "/", { county_name: result['city'], state_code: result['countryName'] });
      // return(result); //! test data here
      
  });

  /* You can also set the locality language as needed */
  reverseGeocoder.localityLanguage='es';

  reverseGeocoder.getClientCoordinates(function(result) {
      console.log(result);
  });
}


function fips_lookup(geolat, geolong) {
	// feeding in long and lat to convert into FIPS and county

	var fips_url =
		"https://geo.fcc.gov/api/census/area?lat=" +
		geolat +
		"&lon=" +
		geolong +
		"&format=json";
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
      document.getElementById("location").value = response.results[0].county_name + " County, " + response.results[0].state_code;
      covid_nametag.innerHTML = "COVID-19 News In " + response.results[0].county_name + " County, " + response.results[0].state_code;
      
      embed_county.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/county-maps/index.html?embed=stateCounty#/county/' + response.results[0].county_fips + '"frameborder="0" scrolling="yes"></iframe>';    
      // document.getElementById("main_post").submit()
      
      document.getElementById("location").value = response.results[0].county_name + " County, " + response.results[0].state_code;
      console.log(document.getElementById("location").value)
      // document.getElementById("main_post").submit()

      $.post( "/", { county_name: response.results[0].county_name, state_code: response.results[0].state_code });
    }
  });
}

