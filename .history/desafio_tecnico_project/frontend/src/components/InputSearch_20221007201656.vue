<script setup>

</script>

<template>
  <div class="autocomplete">
    <input type="text" v-model="state" @input="filterStates"/>
    <ul class="suggestions">
      <li class="suggestion">
        (suggestion)
      </li>

    </ul>
  </div>
</template>

<style>
  .autocomplete {
    position: relative;
  }

  .suggestion {
    padding: 0;
    margin: 0;
    border: 1px solid #eeeeee;
    height: 120px;
    min-height: 1em;
    max-height: 6em;    
    overflow: auto;
  }

  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }

  .autocomplete-result:hover {
    background-color: #4AAE9B;
    color: white;
  }
</style>

