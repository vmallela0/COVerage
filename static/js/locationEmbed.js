var embed_county = document.getElementById('embed')

// getting long and lat
window.onload = function getLocation () {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition)
    } else {
    console.log('null')
  }
  navigator.geolocation.watchPosition(
    function (position) { // location access accepted => loads lat, long into fips_lookup
      console.log('LOCATION ACCESS GRANTED \nLatitude: ' + lat + '\nLongitude: ' + long)
            fips_lookup(lat, long)
    },
    function (error) { // handles location access denied => defaults location to stanford
      if (error.code == error.PERMISSION_DENIED) {
        // alert("Location access was denied. Deafulting location to Stanford, CA...")
        var lat = 37.431313849999995
        var long = -122.16936535498309
        console.log('LOCATION ACCESS DENIED')
                console.log('default latitude: ' + lat + '\ndefault longitude: ' + long)
        fips_lookup(lat, long)
        location_err.innerHTML = 'Location access was denied. Defaulted location to Stanford, CA'
        userlocation.innerHTML = 'COVID-19 News in '
      }
    })

}

function showPosition (position) {
  lat = position.coords.latitude
    long = position.coords.longitude
    fips_lookup()
}

function fips_lookup (geolat, geolong) {
  // feeding in long and lat to convert into FIPS and county

  var fips_url = 'https://geo.fcc.gov/api/census/area?lat=' + geolat + '&lon=' + geolong + '&format=json';
  var settings = {
    async: true,
    crossDomain: true,
    url: fips_url,
    method: 'GET'
  }

  // reading in json object and extracting fips, county and state
  $.ajax(settings).done(function (response) {
    embed_county.innerHTML = '<iframe style="width: 100%; height: 655px" src="https://covid19.biglocalnews.org/county-maps/index.html?embed=stateCounty#/county/' + response.results[0].county_fips + '"frameborder="0" scrolling="yes"></iframe>'
  })
    $.ajax(settings).done(function (response) {
    // console.log(response)
    covid_nametag.innerHTML = 'COVID-19 News In ' + response.results[0].county_name + ' County'
  })
}
