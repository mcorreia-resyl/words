<script setup>
import { ref } from "vue";
import debounce from "./debounce.js";
let results = ref([]);
const search = ref("");

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
    <input class="input" type="text" v-model="search" @input="onInput" />
    <ul class="suggestions" v-show="search.length > 0">
      <li class="suggestion" v-for="(result, i) in results" :key="i">
        {{ result.word }}
      </li>
    </ul>
  </div>
</template>

<style>
.autocomplete {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.input {
  box-sizing: border-box;

  width: 421px;
  height: 51px;


  border: 2px solid #b2bcca;
  border-radius: 10px;
}
.suggestions {
  padding: 0;

  margin: 2%;
  border: 1px solid #eeeeee;
  height: 120px;
  width: 421px;
  min-height: 1em;
  max-height: 50%;
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
