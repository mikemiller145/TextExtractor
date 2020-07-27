
"use strict";
//takes in the json data and parses names found and frequency
function extractData(json_data, titles){
            var chartCount = 1;
            var data = json_data;
            var i = 0;
            var uploadID = data[i]["fields"].upload
            while(i < data.length){
                 uploadID = data[i]["fields"].upload
                 var words = [];
                 var count = [];

                for(var j = i; i < data.length; j++){
                    if(data[j]["fields"].upload !== uploadID){
                        break;
                    }
                    else{
                        words.push(data[j]["fields"].word);
                        count.push(data[j]["fields"].count);
                        i++;
                    }
                }
               createChart(words, count, titles, chartCount)
               chartCount++;

            }

};

//builds n number of charts with the data extracted
function createChart(words, count, titles, num){
            createCanvas(num)
            var ctx = document.getElementById('myChart'+ num).getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: words,
                    datasets: [{
                        label: 'Frequency',
                        data: count,
                        backgroundColor: ['rgb(146, 211, 255)',
                                           'rgb(87, 65, 185)',
                                           'rgb(146, 211, 255)',
                                           'rgb(87, 65, 185)',
                                           'rgb(146, 211, 255)',
                                           'rgb(87, 65, 185)',
                                           'rgb(146, 211, 255)',
                                           'rgb(87, 65, 185)',
                                           'rgb(146, 211, 255)',
                                           'rgb(87, 65, 185)',
                                           ],
                        borderColor: ['rgb(2, 110, 182)',
                                        'rgb(121, 91, 255)',
                                        'rgb(2, 110, 182)',
                                        'rgb(121, 91, 255)',
                                        'rgb(2, 110, 182)',
                                        'rgb(121, 91, 255)',
                                        'rgb(2, 110, 182)',
                                        'rgb(121, 91, 255)',
                                        'rgb(2, 110, 182)',
                                        'rgb(121, 91, 255)',

                        ],
                        borderWidth: 3
                    }]
                },
                options: {
                    legend: {
                    display: false
                    },
                    title: {
                            display: true,
                            text: titles[num-1],
                            fontSize: 25

                        },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            })
           };

//builds the Canvas objects to place the charts
function createCanvas(num){
     var v = document.createElement('canvas');
     v.id="myChart" +num;
     v.style.order = num;
     document.getElementById('charts').appendChild(v);
    };
//Orders the charts newest to oldest
function New(){
    var charts = document.getElementById("charts");
    var length = charts.childNodes.length/2;
    var min = 1;
    if(document.getElementById("myChart" + length).style.order == length){
        for (var i = 1; i < charts.childNodes.length; i++){
            charts.insertBefore(charts.childNodes[i], charts.firstChild);
        }
    };
    for (var i = charts.childNodes.length/2; i > 0; i--){
        document.getElementById("myChart" + i).style.order = min;
        min++;
    }

};

//orders charts oldest to newest
function Old(){
    var charts = document.getElementById("charts");
    var min = 1;
    var length = charts.childNodes.length/2;
    if(document.getElementById("myChart" + length).style.order == min){
        for (var i = 1; i < charts.childNodes.length; i++){
            charts.insertBefore(charts.childNodes[i], charts.firstChild);
        }
    };
    for (var i = charts.childNodes.length/2; i > 0; i--){
        document.getElementById("myChart" + i).style.order = i;
    }

};










