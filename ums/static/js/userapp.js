/*
{
	session
	type:html|json
	content(由type决定内容)
	//jsonContent
	{
		subtype:redirect|form|other
		redirectSubtype
		{
			url
			param
		}
		formSubtype
		{
			action
			method
			inputs[{name, value, type}...]
		}
	}
	

}
*/
function rpcInit()
{

}

function rpc(obj)
{

}

function onSubmit(e)
{
	e.preventDefault();
	var act = e.target.action;
	var pkg = {};
	for(var i in e.target.elements)
	{
		var input = e.target.elements[i];
		pkg[input.name] = input.value;
	}
	pkg['sid'] = $('#s').attr('class');
	console.error(pkg);
	$.post(act,
	pkg, 
	function(data, status)
	{

		console.error("resp ", data);
		if(data.type == 0)
		{
			$('#s').empty();
			$('#s').attr('class', data.session);
			$('#s').append(data.content);
			$('form').submit(onSubmit);
			$('a').click(onHref);
		}
		else
		{

		}
	});
}

function onHref(e)
{
	e.preventDefault();
	var act = e.target.href;
	var pkg = {};
	pkg['sid'] = $('#s').attr('class');
	$.post(act,
		pkg,
		function(data, status)
		{
			console.error('resp ', data);
			if(data.type == 0)
			{
				$('#s').empty();
				$('#s').attr('class', data.session);
				$('#s').append(data.content);
				$('form').submit(onSubmit);
				$('a').click(onHref);
			}
			else
			{

			}
		})
}

function changeWorkPanel(url)
{
	var frame = document.getElementById('work_panel');
	frame.src = url;
}

