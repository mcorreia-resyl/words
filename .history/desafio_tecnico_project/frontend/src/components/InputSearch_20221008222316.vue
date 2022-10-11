<script setup>
import { ref, computed } from "vue";
import debounce from "./debounce.js";
let results = ref([]);
let search = ref("");
const onInput = computed(() => {
  return search.value.length > 0
    ? debounce(() => {
        {
          fetch(`http://127.0.0.1:8000/api?q=` + search.value)
            .then(console.log(search.value.length))
            .then((response) => response.json())
            .then((data) => (results.value = data));
        }
      }, 500)
    : null;
});
</script>

<template>
  <div class="autocomplete">
    <input
      type="text"
      v-model="search"
      v-if="search.length > 0 ? onInput : null"
    />
    <ul v-show="search.length > 0" class="suggestions">
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
