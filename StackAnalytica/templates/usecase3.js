var res = []
const getData = async (language) => {
    console.log("here");
    const response = await fetch('https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&tagged=+language+&site=stackoverflow', {
      method: 'GET'
    });
    const myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
    
    console.log(myJson)
    for ( var i = 0 ; i < 10 ; i++)
    {
        res.push(myJson.items[i]["link"])
    }
    console.log(res)
   
      
    // looping through the data
    var markup = "<h4> List of Trending Question Links </h4>";  
    res.forEach((datarecord, idx) => {
        markup =  markup + createSeries(datarecord, idx);
       
    });
    console.log(markup)
      function createSeries(datarecord, idx) {
        return `
         <ul> <li>${datarecord}</li> </ul>
        `;
      }
  
    var userEmail = document.getElementById("inputEmail3").value;
    if (document.getElementById("gridRadios1").checked)
    {
      console.log("first checked");
      var freq = 1;
    }
    if (document.getElementById("gridRadios2").checked)
    {
      console.log("second checked");
      var freq = 2;
    }
    if (document.getElementById("gridRadios3").checked)
    {
      console.log("Third  checked");
      var freq = 3;
    }
    console.log(markup)
    var template_params = {
    to_name: 'Prakshat Shah',
    message_html:markup
    }
    
    emailjs.send('gmail', 'template_Q1h72yeo', template_params)
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });
    //Code for email frequency
    //setInterval(getData,10000);
}
  
