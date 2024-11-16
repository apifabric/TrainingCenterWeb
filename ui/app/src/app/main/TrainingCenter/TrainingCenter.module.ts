import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {TRAININGCENTER_MODULE_DECLARATIONS, TrainingCenterRoutingModule} from  './TrainingCenter-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    TrainingCenterRoutingModule
  ],
  declarations: TRAININGCENTER_MODULE_DECLARATIONS,
  exports: TRAININGCENTER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class TrainingCenterModule { }