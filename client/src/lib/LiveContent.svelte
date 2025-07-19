<script>
    import { apiData } from "../store.js";

    let options = { 
        weekday: 'long', 
        year: 'numeric', 
        month: '2-digit', 
        day: '2-digit',
        hour: '2-digit', 
        minute: '2-digit', 
        second: '2-digit' 
    };

    // @ts-ignore
    let currentTimestamp = new Date().toLocaleString("en-IN", options)
    setInterval(() => {
        // @ts-ignore
        currentTimestamp = new Date().toLocaleString("en-IN", options)
    }, 1000);

    let currentPrice = "Loading...";
    $: if ($apiData && $apiData.data) {
        currentPrice = $apiData.data[$apiData.data.length - 1];
    }
</script>

<div class="live-content">
    <h3>Current Price : {currentPrice}</h3>
    <em>{currentTimestamp}</em>
</div>

<style>
    .live-content{
        margin-top: 0.5rem;
        width: 300px;
        height: max-content;
    }
    h3{
        font-size: 1rem;
    }
    em{
        font-size: 0.6rem;
        margin-top: 1rem;
    }
</style>
