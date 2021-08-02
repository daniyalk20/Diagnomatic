<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-3 but-section mr-3 shadow p-3 mb-5 bg-body rounded">
        <div class="row">
          <div class="col-6">
            <label class="btn btn-default p-0">
              <input
                type="file"
                accept="image/*"
                ref="file"
                @change="selectImage"
                name="img"
              />
            </label>
          </div>
          <div class="col-6">
            <button
              class="btn btn-success btn-sm float-right"
              :disabled="!currentImage"
              @click="upload"
            >
              Upload
            </button>
          </div>
        </div>
        <div v-if="currentImage" class="progress">
          <div
            class="progress-bar progress-bar-info"
            role="progressbar"
            :aria-valuenow="progress"
            aria-valuemin="0"
            aria-valuemax="100"
            :style="{ width: progress + '%' }"
          >
            {{ progress }}%
          </div>
        </div>
      </div>

      <div class="col img-section ml-3 shadow p-3 mb-5 bg-body rounded">
        <div v-if="previewImage">
          <div>
            <img class="preview my-3" :src="previewImage" alt=""/>
          </div>
        </div>
        <div>
        <div class="alert alert-danger" v-if ="statusPositive">
          <h3>Postive</h3>
        </div>
        <div v-if ="statusNegative">
          <h3>Negative</h3>
        </div>
        <div class="alert alert-warning"  v-if ="statusProcessing">
          <h3>Processing</h3>
        </div>
        <div class="alert alert-info" v-if ="statusNull">
          <h3>Result will be shown here</h3>
        </div>
      </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import UploadService from "@/assets/js/UploadFilesService";
export default {
  data() {
    return {
      currentImage: undefined,
      previewImage: undefined,

      progress: 0,
      statusPositive: '',
      statusNegative: '',
      statusProcessing: '',
      statusNull: '',

      imageInfos: [],
    };
  },
  mounted(){
    this.statusPositive = false,
    this.statusNegative = false,
    this.statusProcessing = false,
    this.statusNull = true
  },
  methods: {
    selectImage() {
      debugger;
      this.currentImage = this.$refs.file.files[0];
      this.previewImage = URL.createObjectURL(this.currentImage);
      this.progress = 0;
      this.status = "";
    },
    upload() {
      this.progress = 0;
      this.statusPositive = true;
      UploadService.upload(this.currentImage, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          this.statusPositive = false;
          this.statusNull = false;
          if(response.data.normal){
            this.statusNegative = true;
          }
          else if(response.data.pneumonia){
            this.status.Positive = true;
          }
          return response.data;
        })
        .then((images) => {
          this.imageInfos = images.data;
        })
        .catch((err) => {
          this.progress = 0;
          this.message = "Could not upload the image! " + err;
          this.currentImage = undefined;
        });
    },
  },
};
</script>

<style>
.body {
  background-color: whitesmoke;
}
.but-section,
.img-section {
  min-height: 500px;
  border-radius: 5px;
}
</style>
