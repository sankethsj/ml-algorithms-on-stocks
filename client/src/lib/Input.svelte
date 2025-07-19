<script>
    import { Chart, registerables } from "chart.js";
    import { apiData } from "../store.js";

    let chartCanvas;
    let chart;

    Chart.register(...registerables);

    $: if ($apiData && chartCanvas) {
        if (chart) {
            chart.destroy();
        }
        renderChart($apiData);
    }

    function renderChart(data) {
        const ctx = chartCanvas.getContext("2d");
        const labels = data.timestamp.map(ts => new Date(ts * 1000).toLocaleDateString());

        chart = new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Historical Price",
                        data: data.data,
                        borderColor: "rgba(75, 192, 192, 1)",
                        backgroundColor: "rgba(75, 192, 192, 0.2)",
                        fill: true,
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
            },
        });
    }
</script>

<div class="input-section">
    <h2>Historical Data (Last 60 Days)</h2>
    <div class="chart-container">
        <canvas bind:this={chartCanvas}></canvas>
    </div>
</div>

<style>
    .input-section {
        width: 100%;
        margin: 2rem 0;
        padding: 1rem;
        background-color: #fff;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h2{
        font-size: 1rem;
    }
    .chart-container {
        width: 100%;
        height: 300px;
        margin-top: 1rem;
    }
</style>
