<script setup>
export default{
  name:'InputSearch'
}
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

