$(document).ready(function(){

    var url = "http://127.0.0.1:5000/"

    $("#saveForm").click(function(){
      $.post(url+"predict",
      getPredictionData(),
      function(data, status){
        var fraud_percentage = parseInt(parseFloat(data)*100)
        $("#fraud_percentage").html(fraud_percentage)
        if (fraud_percentage > 90) {
            $("#fraud_color").attr("class","fraud-red")
        } else if(fraud_percentage > 70){
            $("#fraud_color").attr("class","fraud-yellow")
        } else {
            $("#fraud_color").attr("class","fraud-green")
        }
      });
    });
});

var getPredictionData = function(){
    var arrayPredict =
    {
         CLAIM_NUMBER: $("#claim_number").val(),
         INCIDENT_TYPE:$("#incident_type").val(),
         LOSS_TYPE: $("#loss_type").val(),
         STATE: $("#state").val(),
         LIABILITY: $("#liability").val(),
         SEGMENT: $("#segment").val(),
         INVESTIGATED: $("#investigated").val(),
         LOSS_DATE: $("loss_date").val(),
         INSURED_NAME: $("#insured_name").val(),
         INSURED_AGE: $("#insured_age").val(),
         DEBT: $("#debt").val()
    }
    console.log(arrayPredict)
    return arrayPredict
}