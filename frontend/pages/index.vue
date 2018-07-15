<template>
  <v-app light>
    <v-toolbar dark color="primary">
      <img src="~/static/logo.png" alt="Logo de la archidiócesis">
      <v-toolbar-title id="encabezado">
        <div id="tituloprincipal">
          <span class="titulo">I</span>glesia en
          <span class="titulo">c</span>amino</div>
        <div>Semanario de la Archidiócesis de Mérida-Badajoz (España)</div>
      </v-toolbar-title>
    </v-toolbar>
    <v-content>

        <v-layout column wrap class="mt-1 pt-1" align-center>
 <upload-button title="Subir PDF de revista" :large=true :fileChangedCallback=this.subir_pdf></upload-button>
        </v-layout>

        <section>

        </section>


      <v-footer class="primary">
        <v-layout row wrap>
          <v-flex xs6>
            <div class="white--text  ml-1">
              Director:Juan José Montes
            </div>
          </v-flex>

          <v-flex xs6>
            <div class="white--text align-content-end text-xs-right">
              Correos Electrónicos:
              <a class="white--text" href="mailto:iglenca@meridabadajoz.es">iglenca@meridabadajoz.es</a>,
              <a class="white--text" href="mailto:iglenca@archimeridabadajoz.org">iglenca@archimeridabadajoz.org</a>
            </div>
          </v-flex>
        </v-layout>
      </v-footer>
    </v-content>
  </v-app>



</template>

<script>
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'babel-polyfill'
import colors from 'vuetify/es5/util/colors'
import UploadButton from 'vuetify-upload-button'
Vue.use(Vuetify, {})

export default {
  components: {
   UploadButton
  },
  data: () => ({
    base: '//www.meridabadajoz.net/iglesiaencamino',

  }),

  methods: {
    subir_pdf:function(magazine){
      // alert(magazine.name)
      this.submit_file(magazine)
    },
    submit_file(file){
        let formData = new FormData();

        /*
          Iteate over any file sent over appending the files
          to the form data.
        */
        // for( var i = 0; i < this.files.length; i++ ){
        //   let file = this.files[i];

        //   formData.append('files[' + i + ']', file);
        // }
        formData.append('file', file)

        /*
          Make the request to the POST /select-files URL
        */
        this.$axios.$post( '/upload',
          formData,
          {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
          }
        ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },

  },

  computed: {

  }
}
</script>

<style>
#encabezado {
  width: 100%;
  text-align: center;
  margin-left: -160px;
}

#revistero {
  min-height: 1150px;
}

.titulo {
  color: red;
}
#tituloprincipal {
  text-shadow: 1px 1px 0px black;
  font-family: Baskerville, 'Baskerville Old Face', 'Hoefler Text', Garamond, 'Times New Roman', serif;
  font-size: 1.4em;
}
#revista {
  -webkit-filter: drop-shadow(5px 5px 5px #222);
  filter: drop-shadow(5px 5px 5px #222);
  transform: rotate(-8deg);
}

.container {
  /* min-height: 100vh; */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue',
    Arial, sans-serif;
  /* 1 */
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
