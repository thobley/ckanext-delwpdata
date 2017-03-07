// turn background white on any page other than the homepage

$(document).ready(function(){
   $(".breadcrumb").parent("div").parent("div").parent("div").css("background","#fff");
   var yammerOpts = {
      customButton : true,
      classSelector: "yammer-share",
      defualtMessage: "Check out this dataset on the Data Discovery Portal"
   };
   yam.platform.yammerShare(yammerOpts);


   // remove the content length warnings to do with wfs, they have already been warned at the time
   // of request.
   if($(".alert-error:contains('Content-Length')")){
      $(".alert-error:contains('wfs')").remove()
   }
});
