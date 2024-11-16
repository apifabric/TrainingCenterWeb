import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {EVALUATION_MODULE_DECLARATIONS, EvaluationRoutingModule} from  './Evaluation-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    EvaluationRoutingModule
  ],
  declarations: EVALUATION_MODULE_DECLARATIONS,
  exports: EVALUATION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class EvaluationModule { }