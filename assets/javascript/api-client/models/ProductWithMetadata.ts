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

import { exists, mapValues } from '../runtime';
import type { Price } from './Price';
import {
    PriceFromJSON,
    PriceFromJSONTyped,
    PriceToJSON,
} from './Price';
import type { Product } from './Product';
import {
    ProductFromJSON,
    ProductFromJSONTyped,
    ProductToJSON,
} from './Product';
import type { ProductMetadata } from './ProductMetadata';
import {
    ProductMetadataFromJSON,
    ProductMetadataFromJSONTyped,
    ProductMetadataToJSON,
} from './ProductMetadata';

/**
 * 
 * @export
 * @interface ProductWithMetadata
 */
export interface ProductWithMetadata {
    /**
     * 
     * @type {Product}
     * @memberof ProductWithMetadata
     */
    product: Product;
    /**
     * 
     * @type {ProductMetadata}
     * @memberof ProductWithMetadata
     */
    metadata: ProductMetadata;
    /**
     * 
     * @type {Price}
     * @memberof ProductWithMetadata
     */
    defaultPrice: Price;
    /**
     * 
     * @type {Price}
     * @memberof ProductWithMetadata
     */
    annualPrice: Price;
    /**
     * 
     * @type {Price}
     * @memberof ProductWithMetadata
     */
    monthlyPrice: Price;
}

/**
 * Check if a given object implements the ProductWithMetadata interface.
 */
export function instanceOfProductWithMetadata(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "product" in value;
    isInstance = isInstance && "metadata" in value;
    isInstance = isInstance && "defaultPrice" in value;
    isInstance = isInstance && "annualPrice" in value;
    isInstance = isInstance && "monthlyPrice" in value;

    return isInstance;
}

export function ProductWithMetadataFromJSON(json: any): ProductWithMetadata {
    return ProductWithMetadataFromJSONTyped(json, false);
}

export function ProductWithMetadataFromJSONTyped(json: any, ignoreDiscriminator: boolean): ProductWithMetadata {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'product': ProductFromJSON(json['product']),
        'metadata': ProductMetadataFromJSON(json['metadata']),
        'defaultPrice': PriceFromJSON(json['default_price']),
        'annualPrice': PriceFromJSON(json['annual_price']),
        'monthlyPrice': PriceFromJSON(json['monthly_price']),
    };
}

export function ProductWithMetadataToJSON(value?: ProductWithMetadata | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'product': ProductToJSON(value.product),
        'metadata': ProductMetadataToJSON(value.metadata),
        'default_price': PriceToJSON(value.defaultPrice),
        'annual_price': PriceToJSON(value.annualPrice),
        'monthly_price': PriceToJSON(value.monthlyPrice),
    };
}

