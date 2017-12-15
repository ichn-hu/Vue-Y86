<template>
  <div>
    This is what you see.
    <div :date="date">
      {{ date }}
    </div>
    <v-btn @click="update">
      Click to update
    </v-btn>
  </div>
</template>
<script>
export default {
  data () {
    return {
      date: undefined
    }
  },
  methods: {
    update: function () {
      this.date = Date()
    }
  },
  mounted () {
    this.update()
  }
}
</script>

