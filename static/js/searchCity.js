'use strict';
function initialize() {
      const options = {
        types: ['(cities)']
        };
      const input = document.getElementById('location');
      const autocomplete = new google.maps.places.Autocomplete(input, options);

      autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        document.getElementById('lat').value = place.geometry.location.lat();
        document.getElementById('lng').value = place.geometry.location.lng();
      });
    }