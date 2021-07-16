const remote = require("electron").remote
const axios = require('axios')
const dialog = remote.dialog


// ========== global constants 
let loc = '';
mapping = [ "pop", "metal", "disco", "blues", "reggae", "classical", "rock", "hiphop", "country", "jazz" ]
var loader = document.getElementsByClassName('spinner')[0]



// ========== setup chartjs

var cvs= document.getElementById('myChart')
cvs.style.width = "100%";
cvs.style.height = "300px";

var ctx1 = document.getElementById('myChart').getContext('2d');
let myChart = new Chart(ctx1, {
type: 'bar',
data: {
	labels: mapping,
	datasets: [{
		label: 'Percentage prediction',
		data: [],
		backgroundColor: [
			'rgba(236, 0, 140, 0.5)',
			'rgba(255, 140, 0, 0.5)',
			'rgba(232, 17, 35, 0.5)',
			'rgba(255, 241, 0, 0.5)',
			'rgba(104, 33, 122, 0.5)',
			'rgba(0, 24, 143, 0.5)',
			'rgba(0, 188, 242, 0.5)',
			'rgba(0, 178, 148, 0.5)',
			'rgba(0, 158, 73, 0.5)',
			'rgba(186, 216, 10, 0.5)',
		],
		borderColor: [
			'rgba(236, 0, 140, 1)',
			'rgba(255, 140, 0, 1)',
			'rgba(232, 17, 35, 1)',
			'rgba(255, 241, 0, 1)',
			'rgba(104, 33, 122, 1)',
			'rgba(0, 24, 143, 1)',
			'rgba(0, 188, 242, 1)',
			'rgba(0, 178, 148, 1)',
			'rgba(0, 158, 73, 1)',
			'rgba(186, 216, 10, 1)',
		],
		borderWidth: 1
	}]
},
options: {
	responsive: false,
	scales: {
		y: {
			beginAtZero: true
		}
	}
}
});


function updateChart(arr){
	myChart.data.datasets[0].data = arr;
    myChart.update();
}




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
	cvs.style.display = 'none';
	loader.style.display = 'block';
	document.getElementsByClassName('genre-label')[0].innerHTML = 'None';
}



function submitFile(){
	let params = {
		'path' : loc
	}


	// disable chart and show loader
	loaderFunctionality();


	axios.post('http://localhost:5000/CNN', params, {
		headers: {
			'Content-Type': 'application/json',
		}
	})
	.then(res => {
		let predictions = res.data.predictions[0];
		// console.log(predictions)

		const indexOfMaxValue = predictions.indexOf(Math.max(...predictions));
		// console.log(mapping[indexOfMaxValue])


		// disable loader and show chart 
		loader.style.display = 'none';
		document.getElementsByClassName('genre-label')[0].innerHTML = mapping[indexOfMaxValue];
		cvs.style.display = 'block';
		updateChart(predictions);
	})
	.catch(err => console.log(err));

}
