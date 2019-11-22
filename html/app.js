$(document).ready(function(){

var updateStatus= function(data, status){
                          var fraud_percentage = parseInt(parseFloat(data)*100)
                          $("#fraud_percentage").html(fraud_percentage)
                          if (fraud_percentage > 90) {
                              $("#fraud_color").attr("class","fraud-red")
                          } else if(fraud_percentage > 70){
                              $("#fraud_color").attr("class","fraud-yellow")
                          } else {
                              $("#fraud_color").attr("class","fraud-green")
                          }
                        }
    var url = "http://127.0.0.1:5000/"

    $("#saveForm").click(function(){
      $.post(url+"updaterecord"+$("#claim_number").val(),
      getPredictionDataFromPage(),
      updateStatus
      );
    });

    $("#fetch_claim").click(function(){
          $.get(url+"getrecord/"+$("#claim_number").val(),
          updateStatus);
        });
});

var getPredictionDataFromPage = function(){
    var arrayPredict =
    {
         INCIDENT_TYPE : ("#incident_type").val(),
         Y : ("#y").val(),
         LOSS_TYPE : ("#loss_type").val(),
         STATE : ("#state").val(),
         LIABILITY : ("#liability").val(),
         SEGMENT : ("#segment").val(),
         INVESTIGATED : ("#investigated").val(),
         INSURED_AGE : ("#insured_age").val(),
         DEBT : ("#debt").val(),
         CLAIM_NUMBER : ("#claim_number").val(),
         INSURED_NAME : ("#insured_name").val(),
         policy_inception_days : getDateDiffer(("#loss_date").val(),("#POLICY_EFFECTIVE").val()),
         days_rem_policy_expiry : getDateDiffer(("#policy_expiration").val(),("#loss_date").val()),
         loss_date_month : ("#loss_date").val().substr(5,3),
         loss_date_year : ("#loss_date").val().substr(0,4),
         policy_expiration_month : ("#policy_expiration").val().substr(5,3),
         policy_expiration_year : ("#policy_expiration").val().substr(0,4),
         policy_effective_month : ("#policy_effective").val().substr(5,3),
         policy_effective_year : ("#policy_effective").val().substr(0,4),
         LOSS_DATE : ("#loss_date").val(),
         POLICY_EFFECTIVE : ("#policy_effective").val(),
         POLICY_EXPIRATION : ("#policy_expiration").val(),
         potential_fraudster : ("#potential_fraudster").val(),
         fraud_complete : ("#fraud_complete").val(),
         fraud_risk_level : ("#fraud_risk_level").val(),
         fraud_used : ("#fraud_used").val(),
         location_address : ("#location_address").val(),
         hit_and_run_ind : ("#hit_and_run_ind").val(),
         icbc_keymissingstolen : ("#icbc_keymissingstolen").val(),
         icbc_keyswithvehicle : ("#icbc_keyswithvehicle").val(),
         icbc_numvehiclekeyset : ("#icbc_numvehiclekeyset").val(),
         totalloss : ("#totalloss").val(),
         vehlockind : ("#vehlockind").val(),
         vehstolenind : ("#vehstolenind").val(),
         veh_towed_ind : ("#veh_towed_ind").val(),
         case_status : ("#case_status").val(),
         notes : ("#notes").val(),
         pred_fraud_percent : ("#pred_fraud_percent").val()
    }
    console.log(arrayPredict)
    return arrayPredict
}

var updateFormData = function(data){
        console.log(data)
        jsondata = JSON.parse(data)
        console.log(jsondata)
        debugger;
        $("#incident_type").val(jsondata.INCIDENT_TYPE)
        $("#y").val(jsondata.Y)
        $("#loss_type").val(jsondata.LOSS_TYPE)
        $("#state").val(jsondata.STATE)
        $("#liability_status").val(jsondata.LIABILITY)
        $("#segment").val(jsondata.SEGMENT)
        $("#investigated").val(jsondata.INVESTIGATED)
        $("#insured_age").val(jsondata.INSURED_AGE)
        $("#debt").val(jsondata.DEBT)
        $("#claim_number").val(jsondata.CLAIM_NUMBER)
        $("#insured_name").val(jsondata.INSURED_NAME)
        $("#policy_inception_days").val(jsondata.policy_inception_days)
        $("#days_rem_policy_expiry").val(jsondata.days_rem_policy_expiry)
        $("#loss_date_month").val(jsondata.loss_date_month)
        $("#loss_date_year").val(jsondata.loss_date_year)
        $("#policy_expiration_month").val(jsondata.policy_expiration_month)
        $("#policy_expiration_year").val(jsondata.policy_expiration_year)
        $("#policy_effective_month").val(jsondata.policy_effective_month)
        $("#policy_effective_year").val(jsondata.policy_effective_year)
        $("#loss_date").val(jsondata.LOSS_DATE)
        $("#policy_effective").val(jsondata.POLICY_EFFECTIVE)
        $("#policy_expiration").val(jsondata.POLICY_EXPIRATION)
        $("#potential_fraudster").val(jsondata.potential_fraudster)
        $("#fraud_complete").val(jsondata.fraud_complete)
        $("#fraud_risk_level").val(jsondata.fraud_risk_level)
        $("#fraud_used").val(jsondata.fraud_used)
        $("#location_address").val(jsondata.location_address)
        $("#hit_and_run_ind").val(jsondata.hit_and_run_ind)
        $("#icbc_keymissingstolen").val(jsondata.icbc_keymissingstolen)
        $("#icbc_keyswithvehicle").val(jsondata.icbc_keyswithvehicle)
        $("#icbc_numvehiclekeyset").val(jsondata.icbc_numvehiclekeyset)
        $("#totalloss").val(jsondata.totalloss)
        $("#vehlockind").val(jsondata.vehlockind)
        $("#vehstolenind").val(jsondata.vehstolenind)
        $("#veh_towed_ind").val(jsondata.veh_towed_ind)
        $("#case_status").val(jsondata.case_status)
        $("#notes").val(jsondata.notes)
        $("#pred_fraud_percent").val(jsondata.pred_fraud_percent)


}

function convertDateFormat(dateWithMn){
   var monthsMap = {"Jan" : "01", "Feb" : "02",  "Mar" : "03","Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07","Aug" : "08", "Sep" : "09", "Oct" : "10","Nov" : "11","Dec" : "12"}
   var monthStr = dateWithMn.substr(5,3)

   return dateWithMn.replace(monthStr,monthsMap[monthStr]);
}

function getDateDiffer(dateString1, dateString2) {

    var date1 = new Date(convertDateFormat(dateString1))
    var date2 = new Date(convertDateFormat(dateString2))

   return Math.floor((date2 - date1) / (1000*60*60*24));

}