// Данные графика температуры
let temp = document.getElementById('tempChart').getContext('2d');
let temp_config = {
    type: 'line',

    data: {
     //labels: ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
     datasets: [{
         //data: [26, 24, 27, 30, 26, 23, 25],
         backgroundColor: 'rgba(255, 0, 0, 0.2)'
    }]
},

options: {
    legend: {
        display: false
    },
    title: {
        display: true,
        text:"Температура",
        position: "left",
        fontStyle: "bold"
    }
}

};
let tempChart = new Chart(temp, temp_config);

// Данные графика влажности
let hum = document.getElementById('humChart').getContext('2d');
let hum_config =  {
    type: 'line',

    data: {
     //labels: ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
     datasets: [{
         //data: [12, 19, 3, 5, 2, 3, 7],
         backgroundColor: 'rgba(0, 0, 255, 0.2)'
         
    }]
},

    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text:"Влажность",
            position: "left",
            fontStyle: "bold"
        }
    }
};
let humChart = new Chart(hum, hum_config);