import http from "./http-common";

class UploadFilesService {
  upload(file, onUploadProgress) {

    let formData = new FormData();
    formData.append("file", file);
    console.log(formData.get("file"));
    return http.get("api/pneumonia/", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      },
      onUploadProgress
    });
  }
}

export default new UploadFilesService();