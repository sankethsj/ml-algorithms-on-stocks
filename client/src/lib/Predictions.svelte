<script>
    import { Chart, registerables } from "chart.js";
    import { apiData, prediction } from "../store.js";

    let pred = "Calculating...";
    $: if ($prediction && $prediction.prediction) {
        pred = $prediction.prediction[0]; // Display the first prediction
    }

    let chartCanvas;
    let chart;

    Chart.register(...registerables);

    $: if ($prediction && $apiData && chartCanvas) {
        if (chart) {
            chart.destroy();
        }
        renderChart($apiData, $prediction);
    }

    function getNextTradingDays(lastTimestamp, count) {
        const dates = [];
        let currentDate = new Date(lastTimestamp * 1000);
        while (dates.length < count) {
            currentDate.setDate(currentDate.getDate() + 1);
            const day = currentDate.getDay();
            // Skip weekends (Saturday=6, Sunday=0)
            if (day !== 0 && day !== 6) {
                dates.push(new Date(currentDate.getTime()));
            }
        }
        return dates;
    }

    function renderChart(historicalData, predictionData) {
        const ctx = chartCanvas.getContext("2d");
        
        const last10Timestamps = historicalData.timestamp.slice(-10);
        const last10Labels = last10Timestamps.map(ts => new Date(ts * 1000).toLocaleDateString());
        const last10Data = historicalData.data.slice(-10);

        const futureDates = getNextTradingDays(last10Timestamps[last10Timestamps.length - 1], 5);
        const futureLabels = futureDates.map(date => date.toLocaleDateString());
        
        const combinedLabels = [...last10Labels, ...futureLabels];
        
        const historicalDataset = {
            label: "Historical Price",
            data: last10Data,
            borderColor: "rgba(75, 192, 192, 1)",
            backgroundColor: "rgba(75, 192, 192, 0.2)",
        };

        const predictionDataset = {
            label: "Prediction",
            // Start the prediction line from the last known data point
            data: [
                ...Array(last10Data.length - 1).fill(null), 
                last10Data[last10Data.length - 1], 
                ...predictionData.prediction
            ],
            borderColor: "rgba(255, 99, 132, 1)",
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            fill: false,
            pointRadius: 5,
            pointBackgroundColor: "rgba(255, 99, 132, 1)",
        };

        chart = new Chart(ctx, {
            type: "line",
            data: {
                labels: combinedLabels,
                datasets: [historicalDataset, predictionDataset],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
            },
        });
    }
</script>

<div class="pred-container">
    <h2>Next Day Prediction</h2>
    <div class="prediction-value">
        {pred}
    </div>
    <div class="chart-container">
        <canvas bind:this={chartCanvas}></canvas>
    </div>
</div>

<style>
    .pred-container {
        width: 100%;
        height: max-content;
        margin: 2rem 0;
        padding: 1rem;
        background-color: #fff;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h2{
        font-size: 1rem;
    }
    .prediction-value {
        font-size: 1.4rem;
        font-weight: 700;
        color: oklch(0.5 0.04 192);
        text-align: center;
        margin-bottom: 1rem;
    }
    .chart-container {
        width: 100%;
        height: 300px;
        margin-top: 1rem;
    }
</style>
