<template>
  <v-tooltip top :disabled="operation.length === 0">
    <v-layout row wrap class="m-row mx-1  my-1" slot="activator">
      <v-flex xs2 offset-xs0 class="my-2">
        <m-stage :ins="ins" name="D" :stat="stat" :operation="operation" :bubble="bubble" :stall="stall"></m-stage>
      </v-flex>
      <v-flex xs1 class=" my-2   mx-1 px-0 py-0  ">
        <m-card title="rA" :value="rA"></m-card>
      </v-flex>
      <v-flex xs1 class=" my-2   mx-1  px-0 py-0  ">
        <m-card title="rB" :value="rB"></m-card>
      </v-flex>
      <v-flex xs2 class=" my-2   mx-1  px-0 py-0  ">
        <m-card title="valC" :value="valC"></m-card>
      </v-flex>
      <v-flex xs2 class=" my-2   mx-1  px-0 py-0  ">
        <m-card title="valP" :value="valP"></m-card>
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
    props: ['stat', 'bubble', 'stall', 'ins', 'operation', 'rA', 'rB', 'valC', 'valP']
  }
</script>
<style src="@/assets/stage.css" scoped></style>

