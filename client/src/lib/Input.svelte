<script>
    import { onMount } from "svelte";
    import { apiData } from "../store.js";

    onMount(async () => {
        fetch(
            process.env.API_URL + 'model/input'
        )
            .then((response) => response.json())
            .then((data) => {
                apiData.set(data);
                console.log($apiData.data);
            })
            .catch((error) => {
                console.log(error);
                return [];
            });
    });

    
    
</script>

<div class="input-section">
    Input section
    <div class="chart">

    </div>
</div>

<style>
    .input-section {
        width: 50%;
        margin: 2rem 1rem 2rem 0;
        padding: 1rem;
        background-color: rgb(104, 113, 118);
        border-radius: 1rem;
    }
    .chart {
        width: 100%;
        height: 300px;
        background-color: rgb(67, 78, 83);
    }
</style>
