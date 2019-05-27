// JavaScript Objects are very much like Python Dictionaries
// but Objects do not have " " around keys

var sports = {
	type: "Basketball",
	yearOriginated: 1943,
	numberOfTeams: 32,
	teams: ['lakers', 'celtics', 'warriors', 'trail blazers', 'knicks', 'sixers'],
	conferences: {
		Western: ['lakers', 'warriors'],
		Eastern: ['knicks', 'sixers', 'celtics']
	}
}

// getting keys and values of Object
console.log(Object.keys(sports))
console.log(Object.values(sports))

// indexing specific values
console.log(sports.teams[2])
console.log(sports["teams"][2])

// learn more about Objects
console.dir(Object)
