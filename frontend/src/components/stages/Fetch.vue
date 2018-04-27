<template>
  <v-tooltip top :disabled="operation.length === 0">
    <v-layout row wrap class="m-row mx-1  my-1" slot="activator">
      <v-flex xs2 offset-xs0 class="my-2">
        <m-stage :ins="ins" name="F" :stat="stat" :operation="operation" :bubble="bubble" :stall="stall"></m-stage>
      </v-flex>
      <v-flex xs2 offset-xs2 class=" my-2">
        <m-card title="predPC" :operation="operation" :value="predPC" :bubble="bubble" :stall="stall"></m-card>
      </v-flex>
    </v-layout>
    <span>
      <template>
        <div v-for="c in operation" class="m-operation">
            {{ c }}
        </div>
      </template>
    </span>
  </v-tooltip>
</template>

<script>
  import Stage from '@/components/misc/stage'
  import Card from '@/components/misc/card'
  export default {
    components: {
      'm-stage': Stage,
      'm-card': Card
    },
    name: 'fetch',
    props: ['stat', 'bubble', 'stall', 'ins', 'operation', 'predPC']
  }
</script>
<style src="@/assets/stage.css" scoped></style>
