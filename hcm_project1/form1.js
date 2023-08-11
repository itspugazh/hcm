var user=document.getElementById('#user');
		user.addEventListener('keyup',function ()
		 {
			var u_times.document.querySelector('.u_times');
			var u_check.document.querySelector('.u_check');
			if(user.value.length==0 || user.value.length<6){
				user.style.border="1px red solid";
				u_times.style.display='block';
				u_check.style.display='none';
			}
		})