<script setup>
import {ref} from 'vue'
// const results = await fetch(`/api`.then((r) =>r.json())
const onInput = () =>{
  fetch("https://api.npms.io/v2/search?q=vue")
    .then(response => response.json())
    .then(data => (this.totalVuePackages = data.total));
  
}
</script>

<template>
  <div class="autocomplete">
    <input type="text" v-model="search" @input="onInput" />
    <ul class="suggestions">
      <li class="suggestion"></li>
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
  background-color: #4aae9b;
  color: white;
}
</style>
