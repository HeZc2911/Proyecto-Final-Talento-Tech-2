document.addEventListener('DOMContentLoaded', async function () {
    // URLs de los archivos JSON
    const urls = {
        mujeres: 'assets/Dbs/Asociaciones_Casa_de_la_Mujer_-_Cota.json',
        juvenil: 'assets/Dbs/emprendimiento_juvenil.json',
        negocios: 'assets/Dbs/Negocios_Verdes_20250227.json',
        csv: 'assets/Dbs/csvjson.json'
    };

    // Cargar datos JSON
    async function cargarDatos(url) {
        try {
            const response = await fetch(url);
            return await response.json();
        } catch (error) {
            console.error('Error al cargar datos de:', url, error);
            return [];
        }
    }

    // Obtener datos
    const [mujeresData, juvenilData, negociosData, csvData] = await Promise.all([
        cargarDatos(urls.mujeres),
        cargarDatos(urls.juvenil),
        cargarDatos(urls.negocios),
        cargarDatos(urls.csv)
    ]);

    // Procesar datos para gráficos
    function procesarEmprendimientoFemenino(data) {
        const tipos = {};
        data.forEach(d => {
            if (d["GENERO ASOCIADOS"] === "FEMENINO" || d["GENERO"] === "Femenino") {
                const tipo = d["NOMBRE DE LA ACTIVIDAD"] || "Otros";
                tipos[tipo] = (tipos[tipo] || 0) + 1;
            }
        });
        return tipos;
    }

    function procesarTiposEmprendimiento(data) {
        const tipos = {};
        data.forEach(d => {
            const tipo = d["NOMBRE DE LA ACTIVIDAD"] || d["tipo_de_emprendimiento"] || "Otros";
            tipos[tipo] = (tipos[tipo] || 0) + 1;
        });

        // Agrupar tipos con pocas ocurrencias en "Otros"
        const filteredTipos = {};
        Object.keys(tipos).forEach(key => {
            if (tipos[key] > 1) {
                filteredTipos[key] = tipos[key];
            } else {
                filteredTipos["Otros"] = (filteredTipos["Otros"] || 0) + tipos[key];
            }
        });

        return filteredTipos;
    }

    // Datos estáticos para la tendencia de la innovación (1998-2022)
// Datos estáticos para la tendencia de la innovación (1998-2022)
const tendenciaInnovacion = {
    "1998": 5,
    "1999": 7,
    "2000": 10,
    "2001": 12,
    "2002": 15,
    "2003": 18,
    "2004": 20,
    "2005": 22,
    "2006": 25,
    "2007": 28,
    "2008": 30,
    "2009": 32,
    "2010": 35,
    "2011": 40,
    "2012": 45,
    "2013": 50,
    "2014": 55,
    "2015": 60,
    "2016": 65,
    "2017": 70,
    "2018": 75,
    "2019": 80,
    "2020": 100, // Pico en 2020 (coherente con la base de datos)
    "2021": 85,  // Disminución después del pico
    "2022": 90   // Ligero aumento
};

// Datos estáticos para la comparación emprendimiento vs innovación (2000-2022)
const comparacion = {
    "2000": { emprendimiento: 10, innovacion: 5 },
    "2001": { emprendimiento: 12, innovacion: 6 },
    "2002": { emprendimiento: 15, innovacion: 7 },
    "2003": { emprendimiento: 18, innovacion: 8 },
    "2004": { emprendimiento: 20, innovacion: 10 },
    "2005": { emprendimiento: 22, innovacion: 12 },
    "2006": { emprendimiento: 25, innovacion: 15 },
    "2007": { emprendimiento: 28, innovacion: 18 },
    "2008": { emprendimiento: 30, innovacion: 20 },
    "2009": { emprendimiento: 32, innovacion: 22 },
    "2010": { emprendimiento: 35, innovacion: 25 },
    "2011": { emprendimiento: 40, innovacion: 28 },
    "2012": { emprendimiento: 45, innovacion: 30 },
    "2013": { emprendimiento: 50, innovacion: 32 },
    "2014": { emprendimiento: 55, innovacion: 35 },
    "2015": { emprendimiento: 60, innovacion: 40 },
    "2016": { emprendimiento: 65, innovacion: 45 },
    "2017": { emprendimiento: 100, innovacion: 50 }, // Pico de emprendimiento en 2017
    "2018": { emprendimiento: 75, innovacion: 55 },
    "2019": { emprendimiento: 80, innovacion: 60 },
    "2020": { emprendimiento: 85, innovacion: 100 }, // Pico de innovación en 2020
    "2021": { emprendimiento: 90, innovacion: 85 },
    "2022": { emprendimiento: 95, innovacion: 90 }
};

    // Generar datos para gráficos
    const emprendimientoFemenino = procesarEmprendimientoFemenino([...mujeresData, ...juvenilData]);
    const tiposEmprendimiento = procesarTiposEmprendimiento([...csvData, ...negociosData]);

    // Gráfico de Barras: Emprendimiento Femenino
    new Chart(document.getElementById('barChart').getContext('2d'), {
        type: 'bar',
        data: {
            labels: Object.keys(emprendimientoFemenino),
            datasets: [{
                label: 'Cantidad',
                data: Object.values(emprendimientoFemenino),
                backgroundColor: '#6db4ff',
            }]
        },
        options: { scales: { y: { beginAtZero: true } } }
    });

    // Gráfico de Torta: Tipos de Emprendimiento
    new Chart(document.getElementById('pieChart').getContext('2d'), {
        type: 'pie',
        data: {
            labels: Object.keys(tiposEmprendimiento),
            datasets: [{
                data: Object.values(tiposEmprendimiento),
                backgroundColor: ['#6db4ff', '#3df9ff', '#1f375b', '#d6e7f6', '#ff6d6d', '#ffb46d'],
            }]
        }
    });

    // Gráfico de Líneas: Tendencia de la Innovación
    new Chart(document.getElementById('lineChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: Object.keys(tendenciaInnovacion),
            datasets: [{
                label: 'Innovación',
                data: Object.values(tendenciaInnovacion),
                borderColor: '#6db4ff',
                fill: false,
            }]
        },
        options: { scales: { y: { beginAtZero: true } } }
    });

    // Gráfico de Área: Comparación Emprendimiento vs Innovación
    new Chart(document.getElementById('areaChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: Object.keys(comparacion),
            datasets: [
                {
                    label: 'Emprendimiento',
                    data: Object.values(comparacion).map(d => d.emprendimiento),
                    borderColor: '#6db4ff',
                    fill: true,
                },
                {
                    label: 'Innovación',
                    data: Object.values(comparacion).map(d => d.innovacion),
                    borderColor: '#3df9ff',
                    fill: true,
                }
            ]
        },
        options: { scales: { y: { beginAtZero: true } } }
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
    const url3 = 'assets/Dbs/csvjson.json';
    // Cargar y mapear los datos
    Promise.all([
        fetch(url1).then(response => response.json()),
        fetch(url2).then(response => response.json()),
        fetch(url3).then(response => response.json()),
    ])
    .then(([data1, data2, data3]) => {
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
        const datosMapeados3 = mapearDatos(data3 ,{
            Año: "fecha_de_beneficio_año",
            Nombre: "tipo_de_emprendimiento",
            Género: "sexo",
            Edad: "edad",
            Objeto: "idea_de_negocio"
        });
        // Combinar los datos
        const combinedData = [...datosMapeados1, ...datosMapeados2, ...datosMapeados3];

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
    // Formulario Persona Natural
    document.getElementById('formPersonaNatural').addEventListener('submit', function (e) {
        e.preventDefault();
        let total = 0;
        
        // Sumar todas las respuestas (preguntas 1 a 25)
        for (let i = 1; i <= 25; i++) {
            const value = parseInt(document.getElementById(`pregunta${i}`).value);
            total += value;
        }
        
        // Calcular resultado
        let resultado = '';
        if (total >= 75) {
            resultado = '¡Tienes un alto potencial de emprendimiento! Sigue aprovechando tus habilidades y sigue aprendiendo nuevas estrategias.';
        } else if (total >= 40) {
            resultado = 'Tienes un potencial moderado de emprendimiento. Refuerza tus habilidades, busca mentoría y rodéate de otros emprendedores.';
        } else {
            resultado = 'Necesitas más recursos y apoyo para emprender. Considera cursos de emprendimiento y busca inspiración en casos de éxito.';
        }
        document.getElementById('resultadoPersonaNatural').textContent = resultado;
    });

    // Formulario Líder de Empresa
    document.getElementById('formLiderEmpresa').addEventListener('submit', function (e) {
        e.preventDefault();
        let total = 0;
        
        // Sumar todas las respuestas (preguntas 1 a 15)
        for (let i = 1; i <= 15; i++) {
            const value = parseInt(document.getElementById(`pregunta${i}Empresa`).value);
            total += value;
        }
        
        // Calcular resultado con consejos personalizados
        let resultado = '';
        if (total >= 12) {
            resultado = '¡Tu empresa tiene un alto nivel de innovación! Felicidades, estás liderando el camino en creatividad y desarrollo. Recuerda que la innovación constante mantiene la ventaja competitiva y mejora la satisfacción del cliente. Sigue explorando nuevas tecnologías y fomentando una cultura innovadora en tu equipo.';
        } else if (total >= 7) {
            resultado = 'Tu empresa tiene un nivel moderado de innovación. Vas por buen camino, pero aún hay detalles que mejorar. Considera implementar sesiones de brainstorming, colaboración con startups o inversión en capacitación para potenciar la creatividad de tu equipo.';
        } else {
            resultado = 'Tu empresa necesita más inversión en innovación. La innovación es clave para la competitividad y el crecimiento. Prueba nuevas metodologías como Design Thinking, fomenta la experimentación y apoya a tu equipo en la generación de ideas. También puedes buscar alianzas estratégicas o participar en programas de incubación.';
        }
        document.getElementById('resultadoLiderEmpresa').textContent = resultado;
    });
});