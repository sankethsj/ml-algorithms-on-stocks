<script>
  import "../src/global.css";
  import Header from "../src/lib/Header.svelte";
  import LiveContent from "./lib/LiveContent.svelte";
  import Input from "./lib/Input.svelte";
  import Predictions from "./lib/Predictions.svelte";
</script>

<main>
  <Header />
  <LiveContent />
  <div class="section">
    <Input />
    <Predictions/>
  </div>
  
</main>

<style>
  .section{
    display: flex;
    flex-wrap: wrap;
  }
</style>