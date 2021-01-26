/*
 
Autor: Alejandro Gleason

Lenguaje: JS

Fecha: 18 de feb. de 2020

*/

function mail(mails){
	const results = [];
	for(let email of mails){
		email = email.split('');/*Transforming to array*/
		let domainIndex = email.indexOf('@');
		let domain = email.slice(domainIndex);
		let preDomain = email.slice(0,domainIndex);
		domain = domain.join('');/*I split both the domain and the part that is before the domain*/
		if(preDomain.includes('.')){
			/*Removing all array elements that are .*/
			preDomain = preDomain.filter(elem => elem !== '.');	
		}
		if(preDomain.includes('+')){
			/*Removing everything after the +*/
			let plusIndex = preDomain.indexOf('+');
			preDomain = preDomain.slice(0,plusIndex);
		}
		preDomain = preDomain.join('');
		let finalMail = preDomain + domain;
		if(!results.includes(finalMail)){/*If it does not exists*/
			results.push(finalMail);
		}
	}
	console.log(results.length); /*This is the final result*/
	return results.length;
}

const mails = ["test.email+ignora@bloque9.com","test.e.mail+esto.no.cuenta@bloque9.com","testemail+filtado@gmail.com"];

mail(mails);