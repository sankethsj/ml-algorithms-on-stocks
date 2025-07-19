<script>
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

    let currentPrice = 33524
</script>

<div class="live-content">
    <h3>Current Price : {currentPrice}</h3>
    <em>{currentTimestamp}</em>
</div>

<style>
    .live-content{
        margin-top: 2rem;
        width: max-content;
        height: max-content;
    }
    em{
        margin-top: 1rem;
    }
</style>