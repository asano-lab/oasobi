
let graphID = document.getElementById("graph");

let data = {
    labels: [0,2,4,6,8,10],
    datasets: [{
        label: 'Data 1',
        data: [1,4,2,7,1,6],
        steppedLine: true
    }, {
        label: 'Data 2'
    }] 
}

let options = {
    responsive: false,
    animation: {
        duration: 0,
    },
    title: {
        display: true,
        fontSize: 14,
        fontColor: '#23993d',
        text: 'Graph Title',
    },
    tooltips: {
        mode: 'index',
        intersect: false,
    },
    scales: {
        xAxes: [{
            scaleLabel: {
                display: true,
                fontSize: 14,
                fontColor: 'blue',
                labelString: 'Time',
            },
        }],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Value',
            },
            ticks: {
                min: 0,
                max: 10,
                stepSize: 3,
            }
        }]
    }
}

let myChart = new Chart(graphID, {
    type: 'line',
    data: data,
    options: options,
});

function addData() {
	myChart.data.labels = [2,4,6,8,10,12];
	myChart.data.datasets[0].data = [4,2,7,1,6,9];
	myChart.data.datasets[1].data = [2,9,4,1,2,8];
	myChart.update();
}