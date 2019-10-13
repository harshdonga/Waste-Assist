function check_add(){
    var addr = $('#inputAddress').val()
    if(addr){
    $('#aziz').html('<h4>See Your Location</h4>'+
        '<iframe src="https://www.mapquestapi.com/staticmap/v5/map?key=MRYGgqUTWvlAdwmSxAZyF19gfic1KWzx&locations='+addr+'&size=1100,500@2x" style="width: 930px;height: 550px;"></iframe>');
    }
    else{
        alert("Please Enter Valid Address")
    }
    }