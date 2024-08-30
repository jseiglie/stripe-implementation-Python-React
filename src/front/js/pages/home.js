import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { loadStripe } from '@stripe/stripe-js';
import { Elements } from '@stripe/react-stripe-js';
import { CheckoutForm } from "../component/checkout.jsx";

export const Home = () => {
	const { store, actions } = useContext(Context);
	//la clave en .env!!! ----------- esta de abajo es la clave publica
	const stripePromise = loadStripe(process.env.STRIPE_PROMISE);
	
	
	return (
		<div className="text-center mt-5">
			<h1>Stripe implementation</h1>
			<Elements stripe={stripePromise}>
				<CheckoutForm />
			</Elements>
		</div>
	);
};
