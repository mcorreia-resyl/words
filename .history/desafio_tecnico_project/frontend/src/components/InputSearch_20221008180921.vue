<script setup>
import { ref } from "vue";
import debounce from "./debounce.js";
import { computed } from "@vue/reactivity";
let results = ref([]);
const search = ref("")

const onInput = debounce(() => {
  {if (search.length > 0 { })
    
</script>

<template>
  <div class="autocomplete">
    <input type="text" v-model="search" @input="onInput" />
    <ul class="suggestions">
      <li class="suggestion" v-for="(result, i) in results" :key="i">
        {{ result.word }}
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
  background-color: #4aae9b;
  color: white;
}
</style>
