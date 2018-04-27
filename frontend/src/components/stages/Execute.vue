<template>
  <v-tooltip top :disabled="operation.length === 0">
    <v-layout row wrap class="m-row mx-1  my-1" slot="activator">
      <v-flex xs2 offset-xs0 class="my-2">
        <m-stage :ins="ins" name="E" :stat="stat" :operation="operation" :bubble="bubble" :stall="stall"></m-stage>
      </v-flex>
      <v-flex xs1 class=" my-2  px-0 py-0  mx-1 ">
        <m-card title="valC" :value="valC"></m-card>
      </v-flex>
      <v-flex xs2 class=" my-2  mx-1 px-0 py-0 ">
        <m-card title="valA" :value="valA"></m-card>
      </v-flex>
      <v-flex xs2 class=" my-2  mx-1 px-0 py-0 ">
        <m-card title="valB" :value="valB"></m-card>
      </v-flex>
      <v-flex xs1 class=" my-2  mx-1 px-0 py-0 ">
        <m-card title="dstE" :value="dstE"></m-card>
      </v-flex>
      <v-flex xs1 class=" my-2  mx-1 px-0 py-0 ">
        <m-card title="dstM" :value="dstM"></m-card>
      </v-flex>
      <v-flex xs1 class=" my-2  mx-1 px-0 py-0 ">
        <m-card title="srcA" :value="srcA"></m-card>
      </v-flex>
      <v-flex xs1 class=" my-2  mx-1 px-0 py-0 ">
        <m-card title="srcA" :value="srcA"></m-card>
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
    props: ['stat', 'bubble', 'stall', 'ins', 'operation', 'valC', 'valA', 'valB', 'dstE', 'dstM', 'srcA', 'srcB']
  }
</script>
<style src="@/assets/stage.css" scoped></style>
