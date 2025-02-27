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

function mapearDatos(datos, columnasOriginales) {
    return datos.map(item => {
        return {
            Año: item[columnasOriginales.Año] || "N/A",
            Nombre: item[columnasOriginales.Nombre] || "N/A",
            Género: item[columnasOriginales.Género] || "N/A",
            Edad: item[columnasOriginales.Edad] || "N/A",
            Objeto: item[columnasOriginales.Objeto] || "N/A"
        };
    });
}
document.addEventListener('DOMContentLoaded', function () {
    // URLs de los archivos JSON
    const url1 = 'assets/Dbs/Asociaciones_Casa_de_la_Mujer_-_Cota.json';
    const url2 = 'assets/Dbs/emprendimiento_juvenil.json';

    // Cargar y mapear los datos
    Promise.all([
        fetch(url1).then(response => response.json()),
        fetch(url2).then(response => response.json())
    ])
    .then(([data1, data2]) => {
        // Mapear la primera base de datos
        const datosMapeados1 = mapearDatos(data1, {
            Año: "AÑO DE CONSTITUCIÓN",
            Nombre: "NOMBRE CORPORACIÓN O ASOCIACIÓN",
            Género: "GENERO ASOCIADOS",
            Edad: "EDAD",
            Objeto: "OBJETO DE LA ASOCIACIÓN O CORPORACIÓN"
        });

        // Mapear la segunda base de datos
        const datosMapeados2 = mapearDatos(data2, {
            Año: "FECHA REGISTRO",
            Nombre: "NOMBRE DE LA ACTIVIDAD",
            Género: "GENERO",
            Edad: "EDAD",
            Objeto: "DESCRIPCI�N"
        });

        // Combinar los datos
        const combinedData = [...datosMapeados1, ...datosMapeados2];

        // Inicializar DataTables
        const table = $('#dataTable').DataTable({
            data: combinedData,
            columns: [
                { title: "Año", data: "Año" },
                { title: "Nombre", data: "Nombre" },
                { title: "Género", data: "Género" },
                { title: "Edad", data: "Edad" },
                { title: "Objeto", data: "Objeto" }
            ],
            responsive: true,
            dom: 'Bfrtip',
            buttons: ['copy', 'csv', 'excel', 'pdf', 'print']
        });
    })
    .catch(error => console.error('Error:', error));
});
document.addEventListener('DOMContentLoaded', function () {
    // Formulario para Persona Natural
    document.getElementById('formPersonaNatural').addEventListener('submit', function (e) {
        e.preventDefault();
        const pregunta1 = parseInt(document.getElementById('pregunta1').value);
        const pregunta2 = parseInt(document.getElementById('pregunta2').value);
        const pregunta3 = parseInt(document.getElementById('pregunta3').value);

        const total = pregunta1 + pregunta2 + pregunta3;
        let resultado = '';

        if (total >= 6) {
            resultado = '¡Tienes un alto potencial de emprendimiento!';
        } else if (total >= 3) {
            resultado = 'Tienes un potencial moderado de emprendimiento.';
        } else {
            resultado = 'Necesitas más recursos y apoyo para emprender.';
        }

        document.getElementById('resultadoPersonaNatural').textContent = resultado;
    });

    // Formulario para Líder de Empresa
    document.getElementById('formLiderEmpresa').addEventListener('submit', function (e) {
        e.preventDefault();
        const pregunta1 = parseInt(document.getElementById('pregunta1Empresa').value);
        const pregunta2 = parseInt(document.getElementById('pregunta2Empresa').value);
        const pregunta3 = parseInt(document.getElementById('pregunta3Empresa').value);

        const total = pregunta1 + pregunta2 + pregunta3 + pregunta4 + pregunta5 + pregunta6 + pregunta7 + pregunta8 + pregunta9 + pregunta10 + pregunta11 + pregunta12 + pregunta13 + pregunta14;
        let resultado = '';

        if (total >= 5) {
            resultado = '¡Tu empresa tiene un alto nivel de innovación!';
        } else if (total >= 3) {
            resultado = 'Tu empresa tiene un nivel moderado de innovación.';
        } else {
            resultado = 'Tu empresa necesita más inversión en innovación.';
        }

        document.getElementById('resultadoLiderEmpresa').textContent = resultado;
    });
});