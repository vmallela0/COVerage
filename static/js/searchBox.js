// setup must be done after the search_api is loaded and ready ("load" event triggered)
search_api.on("load", function() {
    // set search_api options
    // all options are set to defaults if this method is omitted
    search_api.setOpts({
        //...options (defaults used for omitted options)...
    });
    
    // define what to do when a location is found
    search_api.on("location-found", function(lastLocationFound) {
        // show alert dialog with location information
        box_data = lastLocationFound,undefined,2[0];
        console.log('from box_data', box_data.x);
        console.log(box_data.y);
        fips_lookup(box_data.y, box_data.x)
        // $.post( "/", {'data': JSON.stringify(lastLocationFound,undefined,2)});
    });
    
    // define what to do when no location is found
    search_api.on("no-result", function() {
        // show alert dialog
        alert("No location matching the entered text could be found.");
    });
    
    // define what to do when a search times out
    search_api.on("timeout", function() {
        // show alert dialog
        alert("The search operation timed out.");
    });
});