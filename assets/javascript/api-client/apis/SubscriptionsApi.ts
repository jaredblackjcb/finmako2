/* tslint:disable */
/* eslint-disable */
/**
 * finmako
 * Finance website with calculators to support decision making.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import type {
  CreateCheckout,
  ProductWithMetadata,
} from '../models';
import {
    CreateCheckoutFromJSON,
    CreateCheckoutToJSON,
    ProductWithMetadataFromJSON,
    ProductWithMetadataToJSON,
} from '../models';

export interface CreateCheckoutSessionRequest {
    createCheckout: CreateCheckout;
}

/**
 * 
 */
export class SubscriptionsApi extends runtime.BaseAPI {

    /**
     */
    async activeProductsListRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<ProductWithMetadata>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // ApiKeyAuth authentication
        }

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/subscriptions/api/active-products/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => ProductWithMetadataFromJSON(jsonValue));
    }

    /**
     */
    async activeProductsList(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<ProductWithMetadata> {
        const response = await this.activeProductsListRaw(initOverrides);
        return await response.value();
    }

    /**
     */
    async createCheckoutSessionRaw(requestParameters: CreateCheckoutSessionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<string>> {
        if (requestParameters.createCheckout === null || requestParameters.createCheckout === undefined) {
            throw new runtime.RequiredError('createCheckout','Required parameter requestParameters.createCheckout was null or undefined when calling createCheckoutSession.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // ApiKeyAuth authentication
        }

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/subscriptions/stripe/api/create-checkout-session/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: CreateCheckoutToJSON(requestParameters.createCheckout),
        }, initOverrides);

        return new runtime.TextApiResponse(response) as any;
    }

    /**
     */
    async createCheckoutSession(requestParameters: CreateCheckoutSessionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<string> {
        const response = await this.createCheckoutSessionRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async createPortalSessionRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<string>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // ApiKeyAuth authentication
        }

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/subscriptions/stripe/api/create-portal-session/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.TextApiResponse(response) as any;
    }

    /**
     */
    async createPortalSession(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<string> {
        const response = await this.createPortalSessionRaw(initOverrides);
        return await response.value();
    }

}
