<script>
  import { onMount } from "svelte";
  import { apiData, prediction } from "./store.js";
  import "../src/global.css";
  import Header from "../src/lib/Header.svelte";
  import LiveContent from "./lib/LiveContent.svelte";
  import Input from "./lib/Input.svelte";
  import Predictions from "./lib/Predictions.svelte";

  onMount(async () => {
    try {
      const res = await fetch(process.env.API_URL + "/model/input");
      const data = await res.json();
      apiData.set(data);

      const predRes = await fetch(process.env.API_URL + "/model/predict");
      const predData = await predRes.json();
      prediction.set(predData);
    } catch (error) {
      console.error("Failed to fetch data:", error);
    }
  });
</script>

<main>
  <div class="top-section">
    <Header />
    <LiveContent />
  </div>
  <Predictions/>
  <Input />
</main>

<style>
  .top-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.3rem;
  }
</style>
