//Joshua Jaja - 1664245
// CIS 3368 - 16242 - Dobretsberger
// HW3 - EJS, API and Forms - Spring 2022

// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');

var selectedID = "";
app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// index page 
app.get('/', function(req, res) {
    res.render('pages/index') // runs index page on startup
});

app.post('/processdynamicform', function(req, res){
    //check argument from form
    console.log(req.body);
    hero = req.body; // assign dictionary to name
    hero = hero["superhero"]; // hero = superhero name, not nested in anything
    hero_tagline = "Aliases for: " + hero // tagline to present based on hero name

    //superhero API CALL
    axios.get('https://superheroapi.com/api/4156805224424889/search/' + hero) // combine hero for search term
    .then((response)=>{
        hero_data = response.data["results"] // store hero results in var
        
        hero_info = [] // hero_info if wanted to add more than just name
        for (x in hero_data) { // iterate through alter egos
            const obj = hero_data[x] // obj is item in hero_data
            let bio = obj.biography // biography set to bio
            let image = obj.image // image set to image from results
            hero_info.push({ // append dict with name to hero_info
                name: bio["aliases"],
                img: image["url"]
            });
        }
        console.log(hero_info) // log to console to check nested arrray
        
        res.render('pages/index', {
            hero_info: hero_info, // pass through hero_info
            hero_tagline: hero_tagline // pass through hero_tagline
        }); 
    });
});

app.listen(8080);
console.log('8080 is the magic port');