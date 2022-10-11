<script setup>
export default {
}
</script>

<template>
  <div class="autocomplete">
    <input type="text" v-model="search" @input="onChange"/>
    <ul class="suggestions">
      <li class="suggestion">
      </li>

    </ul>
  </div>
</template>

<style>
  .autocomplete {
    position: relative;
  }

  .suggestions {
    padding: 0;
    margin: 0;
    border: 1px solid #eeeeee;
    height: 120px;
    min-height: 1em;
    max-height: 6em;    
    overflow: auto;
  }

  .suggestion {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }

  .suggestion:hover {
    background-color: #4AAE9B;
    color: white;
  }
</style>

