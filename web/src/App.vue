<template>
  <v-app id="inspire">
    <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="blue darken-3"
      dark
    >
      <v-toolbar-title
        class="ml-0 pl-4"
      >
        <span class="hidden-sm-and-down">Hifuzion Financeiro</span>
      </v-toolbar-title>
      <v-spacer />

      <v-btn
        text
        :to="rota.path"
        v-for="rota in $router.options.routes"
        :key="rota.path"
      >
        {{rota.name}}
      </v-btn>

    </v-app-bar>

    <v-content>
      <v-container>
        <router-view />
      </v-container>
    </v-content>
  </v-app>
</template>
