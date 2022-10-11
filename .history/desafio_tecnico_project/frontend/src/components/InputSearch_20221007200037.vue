<script setup>
export default {
  data: function() {
    return{
      state: ''
      states: ["Lisboa"
      ]
    }
  }
}
</script>

<template>
  <div>
    <input type="text" v-model="state" @input="filterStates/>
  </div>
</template>

