document.addEventListener('DOMContentLoaded', function () {
    // Gráfico de Barras: Emprendimiento Femenino
    const barChartCtx = document.getElementById('barChart').getContext('2d');
    const barChart = new Chart(barChartCtx, {
        type: 'bar',
        data: {
            labels: ['Tecnología', 'Moda', 'Alimentos', 'Servicios'],
            datasets: [{
                label: 'Emprendimiento Femenino',
                data: [120, 80, 150, 90],
                backgroundColor: ['#6db4ff', '#3df9ff', '#1f375b', '#d6e7f6'],
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Gráfico de Torta: Tipos de Emprendimiento en Colombia
    const pieChartCtx = document.getElementById('pieChart').getContext('2d');
    const pieChart = new Chart(pieChartCtx, {
        type: 'pie',
        data: {
            labels: ['Social', 'Tecnológico', 'Cultural', 'Empresarial'],
            datasets: [{
                label: 'Tipos de Emprendimiento',
                data: [40, 30, 20, 10],
                backgroundColor: ['#6db4ff', '#3df9ff', '#1f375b', '#d6e7f6'],
            }]
        }
    });

    // Gráfico de Líneas: Tendencia de la Innovación
    const lineChartCtx = document.getElementById('lineChart').getContext('2d');
    const lineChart = new Chart(lineChartCtx, {
        type: 'line',
        data: {
            labels: ['2010', '2015', '2020', '2023'],
            datasets: [{
                label: 'Innovación Global',
                data: [50, 70, 90, 120],
                borderColor: '#6db4ff',
                fill: false,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Gráfico de Área: Comparación Emprendimiento vs Innovación
    const areaChartCtx = document.getElementById('areaChart').getContext('2d');
    const areaChart = new Chart(areaChartCtx, {
        type: 'line',
        data: {
            labels: ['2010', '2015', '2020', '2023'],
            datasets: [
                {
                    label: 'Emprendimiento',
                    data: [30, 50, 70, 90],
                    borderColor: '#6db4ff',
                    fill: true,
                },
                {
                    label: 'Innovación',
                    data: [40, 60, 80, 100],
                    borderColor: '#3df9ff',
                    fill: true,
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Encuesta de Capacidad de Emprendimiento
    document.getElementById('encuestaForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const pregunta1 = parseInt(document.getElementById('pregunta1').value);
        const pregunta2 = parseInt(document.getElementById('pregunta2').value);
        const pregunta3 = parseInt(document.getElementById('pregunta3').value);

        const total = pregunta1 + pregunta2 + pregunta3;
        let resultado = '';

        if (total === 3) {
            resultado = '¡Tienes un alto potencial de emprendimiento!';
        } else if (total >= 1) {
            resultado = 'Tienes un potencial moderado de emprendimiento.';
        } else {
            resultado = 'Necesitas más recursos y apoyo para emprender.';
        }

        document.getElementById('resultadoEncuesta').textContent = resultado;
    });
});