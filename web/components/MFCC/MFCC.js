const remote = require("electron").remote
const axios = require('axios')
const dialog = remote.dialog


let loc = '';
var loader = document.getElementsByClassName('spinner')[0]

// ========== Functions 

function showFileBox(){
	dialog.showOpenDialog(remote.getCurrentWindow(), {
		properties: ["openFile"]
	}).then(result => {
		if (result.canceled === false) {
			let temp_arr = result.filePaths[0].split('/');
			let short_filename = temp_arr[temp_arr.length -1];
			document.getElementById('select-button').innerHTML = short_filename;

			loc = result.filePaths;
		}
	}).catch(err => {
		console.log(err)
	})
}


function loaderFunctionality(){
	// disable images
	let images = document.getElementsByClassName('fetched-img');
	for(let i=0; i<5; ++i){
		images[i].style.display = 'none';
	}

	loader.style.display = 'block';

	// remove data-label
	document.getElementsByClassName('data-label')[0].style.display = 'inline'
}



function submitFile(){
	let params = {
		'path' : loc
	}

	// disable images and show loader
	loaderFunctionality();

	axios.post('http://localhost:5000/MFCC', params, {
		headers: {
			'Content-Type': 'application/json',
		}
	})
	.then(res => {
		// disable loader and show images 
		let images = document.getElementsByClassName('fetched-img');
		for(let i=0; i<5; ++i){
			images[i].style.display = 'block';
		}
		loader.style.display = 'none';
		// remove data-label
		document.getElementsByClassName('data-label')[0].style.display = 'none'


		// console.log(res.data.plots)
		images[0].src = 'data:image/png;base64, ' + res.data.plots[0];
		images[1].src = 'data:image/png;base64, ' + res.data.plots[1];
		images[2].src = 'data:image/png;base64, ' + res.data.plots[2];
		images[3].src = 'data:image/png;base64, ' + res.data.plots[3];
		images[4].src = 'data:image/png;base64, ' + res.data.plots[4];

		for(let i=0; i<5; ++i){
			images[i].style.width = '100%';
			images[i].style.height = '300px';
		}

	})
	.catch(err => console.log(err));

}
