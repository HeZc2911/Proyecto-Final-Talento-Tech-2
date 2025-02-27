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

document.addEventListener('DOMContentLoaded', function () {
    // Cargar los datos desde los archivos JSON
    fetch('assets/Dbs/Asociaciones_Casa_de_la_Mujer_-_Cota.json')
        .then(response => response.json())
        .then(data => {
            const table = $('#dataTable').DataTable({
                data: data,
                columns: [
                    { data: 'AÑO DE CONSTITUCIÓN', title: 'Año' },
                    { data: 'NOMBRE CORPORACIÓN O ASOCIACIÓN', title: 'Nombre' },
                    { data: 'GENERO ASOCIADOS', title: 'Género' },
                    { data: 'EDAD', title: 'Edad' },
                    { data: 'OBJETO DE LA ASOCIACIÓN O CORPORACIÓN', title: 'Objeto' }
                ],
                responsive: true,
                dom: 'Bfrtip',
                buttons: [
                    'copy', 'csv', 'excel', 'pdf', 'print'
                ]
            });
        });

    fetch('assets/Dbs/emprendimiento_juvenil.json')
        .then(response => response.json())
        .then(data => {
            const table = $('#dataTable').DataTable({
                data: data,
                columns: [
                    { data: 'FECHA REGISTRO', title: 'Fecha' },
                    { data: 'DEPENDENCIA GESTORA', title: 'Dependencia' },
                    { data: 'EDAD', title: 'Edad' },
                    { data: 'GÉNERO', title: 'Género' },
                    { data: 'NIVEL DE EDUCACIÓN', title: 'Educación' },
                    { data: 'TIPO DE USUARIO', title: 'Tipo de Usuario' },
                    { data: 'NOMBRE DE LA ACTIVIDAD', title: 'Actividad' },
                    { data: 'DESCRIPCIÓN', title: 'Descripción' }
                ],
                responsive: true,
                dom: 'Bfrtip',
                buttons: [
                    'copy', 'csv', 'excel', 'pdf', 'print'
                ]
            });
        });
});
document.addEventListener('DOMContentLoaded', function () {
    // Cargar los datos desde los archivos JSON
    fetch('assets/Dbs/Asociaciones_Casa_de_la_Mujer_-_Cota.json')
        .then(response => response.json())
        .then(data => {
            const table = $('#dataTable').DataTable({
                data: data,
                columns: [
                    { data: 'AÑO DE CONSTITUCIÓN', title: 'Año' },
                    { data: 'NOMBRE CORPORACIÓN O ASOCIACIÓN', title: 'Nombre' },
                    { data: 'GENERO ASOCIADOS', title: 'Género' },
                    { data: 'EDAD', title: 'Edad' },
                    { data: 'OBJETO DE LA ASOCIACIÓN O CORPORACIÓN', title: 'Objeto' }
                ],
                responsive: true,
                dom: 'Bfrtip',
                buttons: [
                    'copy', 'csv', 'excel', 'pdf', 'print'
                ],
                initComplete: function () {
                    this.api().columns().every(function () {
                        var column = this;
                        var select = $('<select><option value=""></option></select>')
                            .appendTo($(column.footer()).empty())
                            .on('change', function () {
                                var val = $.fn.dataTable.util.escapeRegex(
                                    $(this).val()
                                );

                                column
                                    .search(val ? '^' + val + '$' : '', true, false)
                                    .draw();
                            });

                        column.data().unique().sort().each(function (d, j) {
                            select.append('<option value="' + d + '">' + d + '</option>')
                        });
                    });
                }
            });
        });
});


