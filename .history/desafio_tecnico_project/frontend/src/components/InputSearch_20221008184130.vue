<script setup>
import { ref } from "vue";
import debounce from "./debounce.js";
let results = ref([]);
let search = ref("")

const onInput = debounce(() => {
  {
    fetch(`http://127.0.0.1:8000/api?q=` + search.value)
      .then((response) => response.json())
      .then((data) => (results.value = data));
  }
}, 500);

</script>

<template>
  <div class="autocomplete">
    <input type="text" v-model="search" {search.value.length ? @input="onInput" />
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
