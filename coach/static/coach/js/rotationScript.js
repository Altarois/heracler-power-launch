$(".panel").hide();
console.log("is working")
var angle = 0;

$('.show').click(function(){
   $(this).parents(".show").find(".hideb").slideToggle(150);
   $(this).parents(".show").find(".close").css({"transform": "rotate(180deg)" });
  
  //hide parent and show next
  console.log("legmi");
  
});

 $(function(){
    $(".flip").on("click",function(){
      $(this).next().slideToggle(1000);
      $(this).parents().find(".close").toggleClass("down");
     // $(this).parents().find(".close").css({"transform": "rotate(+180deg)" });
      angle +=180;
      
       
      
    });
 });
