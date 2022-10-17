<script setup>
import { ref } from "vue";
import debounce from "./debounce.js";
let results = ref([]);
const search = ref("");

const onInput = debounce(() => {
  {
    fetch(`http://127.0.0.1:8000/api?q=` + search.value).then(
      (data) => (results = data)
    );
  }
}, 500);
</script>

<template>
  <div class="autocomplete">
    <input
      class="input"
      placeholder="Enter a word"
      type="text"
      v-model="search"
      @input="onInput"
    />
    <ul class="suggestions" v-show="search.length > 0" v-for="(result, i) in results" :key="i">
      <li class="suggestion" >
        {{ result }}
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
  padding: 4px 10px;

  border: 2px solid #b2bcca;
  border-radius: 5px;
}
.suggestions {
  padding: 0;

  margin: 2%;
  border: 1px solid #eeeeee;
  width: 421px;
  min-height: 1em;
  max-height: 300px;
  overflow: auto;
  border: 2px solid #b2bcca;
  border-radius: 5px;
}

.suggestion {
  list-style: none;
  text-align: left;
  padding: 4px 10px;
  cursor: pointer;
}

.suggestion:hover {
  background-color: #4aae9b;
  color: white;
}
</style>
